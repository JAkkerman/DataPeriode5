// Joos Akkerman (11304723)
// Data Processing Week 6
// This file visualizes two graphs that are linked

// set properties of barchart, scalable to w (width) and h (height)
var w = 750;
var h = 350;
var start_w = 60;
var end_w = 0.9*w;
var start_h = 10;
var end_h = 0.85*h;
var barPadding = 2;

d3v5.json('data.json').then(function(data){

  console.log(data['OECD'])
  drawBarChart(data['OECD'])

  addFillKey(data)

  var map = new Datamap({
    element: document.getElementById("map"),
    data: data,
    fills: {
      good: 'rgb(0, 252, 1)',
      decent: 'rgb(178, 254, 1)',
      acceptable: 'rgb(176, 252, 99)',
      not_good: 'rgb(231, 252, 99)',
      bad: 'rgb(162, 106, 75)',
      defaultFill: '#b0b3b7',
    },
    geographyConfig: {
      popupTemplate: function(geography, data) {
        data.forEach(function(element) {
          if (element['YEAR'] == 2016) {
            value = element['VALUE']
          }
        })
        return ["<div class='hoverinfo'>", geography.properties.name,': ', value, "</div>"].join('');
      },
    },
    done: function(datamap) {
        datamap.svg.selectAll('.datamaps-subunit').on('click', function(geography) {
          if (typeof(data[geography.id]) != 'undefined') {
            // console.log(data[geography.id])
            for (var year in data[geography.id]) {
              // console.log(data[geography.id][year]['YEAR'])
            }
            // console.log(data[geography.id]);
            d3v5.selectAll(".barChart").remove()
            drawBarChart(data[geography.id]);
          }
        });
    }
  });

})

function drawBarChart(countrydata) {
  console.log(countrydata);

  countrydata.forEach(function(data){
    console.log(data['VALUE'])
  })

  var svg = d3v5.select("body")
    .append("svg")
    .attr("class", "barChart")
    .attr("width", w)
    .attr("height", h);

  // sets the country names on the x-axis
  var xScale = d3v5.scaleBand()
                 .domain([1960, 2016])
                 .range([start_w, end_w]);

  // sets the scale for the y-axis
  var yScale = d3v5.scaleLinear()
                 .domain([100, 0])
                 .range([start_h, end_h - start_h]);

  // initiate x-axis and y-axis
  var xAxis = d3v5.axisBottom(xScale);
  var yAxis = d3v5.axisLeft(yScale);

  svg.selectAll("rect")
    .data(countrydata)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("y", function(d) {
      if (d["VALUE"] == 'undefined') {
        value = start_h
      }
      else {
        value = d["VALUE"] + start_h
      }
      return start_h + yScale(value);
    })
    .attr("width", (end_w - start_w) / countrydata.length - barPadding)
    .attr("height", function(d) {
        return end_h - start_h - yScale(value);
    })
    .attr("x", function(d, i) {
        return start_w + i * ((end_w - start_w) / countrydata.length);
    });

  // draw both axes
  svg.append("g")
     .attr("transform", "translate(0, "+ end_h +")")
     .call(xAxis);

  svg.append("g")
     .attr("transform", "translate("+ start_w +", "+ start_h +")")
     .call(yAxis);

   // set axis titles
   svg.append("text")
      .attr("x", w/2 - start_w)
      .attr("y", h)
      .text("Years");

   svg.append("text")
      .attr("x", -end_h/2)
      .attr("y", start_w/2)
      .attr("text-anchor", "middle")
      .attr("transform", "rotate(-90)")
      .text("Percentage renewable energy");

}

function addFillKey(data) {
  for (datum in data){
    data[datum].forEach(function(element) {
      if (element['YEAR'] == 2016) {
        if (element["VALUE"] > 60) {
          data[datum].fillKey = 'good';
        }
        else if (element["VALUE"] > 30) {
          data[datum].fillKey = 'decent';
        }
        else if (element['VALUE'] > 15) {
          data[datum].fillKey = 'acceptable';
        }
        else if (element['VALUE'] > 7) {
          data[datum].fillKey = 'not_good';
        }
        else {
          data[datum].fillKey = 'bad';
        }
      }
    })
    // console.log(data)
  }
}
