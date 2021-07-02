if(document.getElementById("t1_percent")!=null){
var data = {
  datasets: [{
      data: [
          document.getElementById("t1_percent").innerHTML,
          document.getElementById("t2_percent").innerHTML
      ],
      backgroundColor: [
        document.getElementById("t1_clr").innerHTML,
        document.getElementById("t2_clr").innerHTML
      ],
      borderWidth:0,
      label: 'My dataset', // for legend
      // backgroundColor:['red','yellow'],
     
  }],
  labels: [
    document.getElementById("t1_name").innerHTML,
    document.getElementById("t2_name").innerHTML,
    
  ],
};


var pieOptions = {
  layout:{
    padding:{
      left:10,right:10,top:10,bottom:10
    }
  },
  "legend": {
    "display": true,
    "labels": {
        "fontSize": 20,
         "fontColor":"black"
    }
},
responsive:false,
events: false,
animation: {
  duration: 5000,
  easing: "easeOutQuart",
  onComplete: function () {
    
    var ctx = this.chart.ctx;
    // ctx.font = Chart.helpers.fontString(Chart.defaults.global.defaultFontFamily, 'normal', Chart.defaults.global.defaultFontFamily);
    var fontsize = 2;
    ctx.font=fontsize +"em Verdana";

    ctx.textAlign = 'center';
    ctx.textBaseline = 'bottom';

    this.data.datasets.forEach(function (dataset) {

      for (var i = 0; i < dataset.data.length; i++) {
        var model = dataset._meta[Object.keys(dataset._meta)[0]].data[i]._model,
            total = dataset._meta[Object.keys(dataset._meta)[0]].total,
            mid_radius = model.innerRadius + (model.outerRadius - model.innerRadius)/2,
            start_angle = model.startAngle,
            end_angle = model.endAngle,
            mid_angle = start_angle + (end_angle - start_angle)/2;

        var x = mid_radius * Math.cos(mid_angle);
        var y = mid_radius * Math.sin(mid_angle);

        ctx.fillStyle = 'black';
        var percent = String(Math.round(dataset.data[i]/total*100)) + "%";      
        //Don't Display If Legend is hide or value is 0
        if(dataset.data[i] != 0 && dataset._meta[0].data[i].hidden != true) {
          // Display percent in another line, line break doesn't work for fillText
          ctx.fillText(percent, model.x + x, model.y + y + 15);
        }
      }
    });
    
               
  }
},

};

var pieChartCanvas = document.getElementById("myChart");
var pieChart = new Chart(pieChartCanvas, {
type: 'pie', // or doughnut
data: data,
options: pieOptions
});
}