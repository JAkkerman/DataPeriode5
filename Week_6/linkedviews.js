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

  // draw bar chart of average OECD data
  drawBarChart(['OECD', data['OECD']])

  // determine colors of countries, based on degree of sustainable energy
  addFillKey(data)

  // draw map
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
        // show country name and sustainability value when hovering
        data.forEach(function(element) {
          if (element['YEAR'] == 2016) {
              value = element['VALUE']
          }
        })
        return ["<div class='hoverinfo'>", geography.id,': ', value, "</div>"].join('');
      },
    },
    done: function(datamap) {
        datamap.svg.selectAll('.datamaps-subunit').on('click', function(geography) {
          // draw bar chart if user clicks on country
          if (typeof(data[geography.id]) != 'undefined') {
            d3v5.selectAll(".barChart").remove()
            drawBarChart([geography.properties.name, data[geography.id]]);
          }
        });
    }
  });

})

function drawBarChart([name, countrydata]) {
  // draws bar chart of selected country

  // allows hover over individual bars and shows values
  var tip = d3v5.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
      return "Renewable Energy in "+ d["YEAR"] +": <strong>" + d["VALUE"] + "</strong> %</span>";
  });

  // appends svg of bar chart
  var svg = d3v5.select("body")
    .append("svg")
    .attr("class", "barChart")
    .attr("width", w)
    .attr("height", h);

  // sets the country names on the x-axis
  var xScale = d3v5.scaleTime()
                 .domain([new Date(1960, 0, 1), new Date(2016, 0, 1)])
                 .range([start_w, end_w]);

  // sets the scale for the y-axis
  var yScale = d3v5.scaleLinear()
                 .domain([100, 0])
                 .range([start_h, end_h - start_h]);

  // initiate x-axis and y-axis
  var xAxis = d3v5.axisBottom(xScale);
  var yAxis = d3v5.axisLeft(yScale);

  // draws bar for each year in data set
  svg.selectAll("rect")
    .data(countrydata)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("y", function(d) {
      return start_h + yScale(d["VALUE"]);
    })
    .attr("width", (end_w - start_w) / countrydata.length - barPadding)
    .attr("height", function(d) {
        if (d["VALUE"] == 'undefined') {
          return 0;
        }
        else {
          return end_h - start_h - yScale(d["VALUE"]);
        }
    })
    .attr("x", function(d, i) {
        return start_w + i * ((end_w - start_w) / countrydata.length);
    })
    .attr("fill", function(d) {
        if (d["VALUE"] > 60) {
          return "rgb(0, 252, 1)";
        }
        else if (d["VALUE"] > 30) {
           return "rgb(178, 254, 1)";
        }
        else if (d["VALUE"] > 15) {
          return "rgb(176, 252, 99)";
        }
        else if (d["VALUE"] > 7) {
          return "rgb(231, 252, 99)";
        }
        else {
          return "rgb(162, 106, 75)";
        }
      })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);

  svg.call(tip);

  // draw both axes
  svg.append("g")
     .attr("transform", "translate(0, "+ end_h +")")
     .call(xAxis);

  svg.append("g")
     .attr("transform", "translate("+ start_w +", "+ start_h +")")
     .call(yAxis);

   // set axis titles and title of bar chart, which is the name of the country
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

    svg.append("text")
       .attr("x", w/2 - start_w)
       .attr("y", start_h + 5)
       .text(name);

}

function addFillKey(data) {
  // adds color to countries based on their level of sustainability

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
        };
      };
    });
  };
};
