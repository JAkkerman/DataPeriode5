// Joos Akkerman (11304723)
// Data Processing Week 5

// set API adresses for used data
var teensInViolentArea = "https://stats.oecd.org/SDMX-JSON/data/CWB/AUS+AUT+BEL+BEL-VLG+CAN+CHL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+OAVG+NMEC+BRA+BGR+CHN+COL+CRI+HRV+CYP+IND+IDN+MLT+PER+ROU+RUS+ZAF.CWB11/all?startTime=2010&endTime=2017";
var teenPregnancies = "https://stats.oecd.org/SDMX-JSON/data/CWB/AUS+AUT+BEL+BEL-VLG+CAN+CHL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+OAVG+NMEC+BRA+BGR+CHN+COL+CRI+HRV+CYP+IND+IDN+MLT+PER+ROU+RUS+ZAF.CWB46/all?startTime=1960&endTime=2017";
var dataGDP = "https://stats.oecd.org/SDMX-JSON/data/SNA_TABLE1/AUS+AUT+BEL+CAN+CHL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EU28+EU15+OECDE+OECD+OTF+NMEC+ARG+BRA+BGR+CHN+COL+CRI+HRV+CYP+IND+IDN+MLT+ROU+RUS+SAU+ZAF+FRME+DEW.B1_GE.HCPC/all?startTime=2012&endTime=2018&dimensionAtObservation=allDimensions";
var requests = [d3.json(teensInViolentArea), d3.json(teenPregnancies), d3.json(dataGDP)];

// set properties for the graph
var w = 900;
var h = 550;
var start_w = 60;
var end_w = 0.85*w;
var start_h = 40;
var end_h = 0.85*h;
var end_y = 50;
var end_x = 35;
var barPadding = 2;
var startyear = year = 2012;
var endyear = 2015;
var colors = ['#dbd87a', '#a1dab4', '#41b6c4', '#225ea8'];

window.onload = function() {

  Promise.all(requests).then(function(response) {

    // get data in JSON format
    var teenViolentData = transformResponse(response[0]);
    var teenPregData = transformResponse(response[1]);
    var dataGDP = transformResponseGDP(response[2]);

    // clean data
    converted_data = convert(teenViolentData, teenPregData, dataGDP);

    // set scales and draw the first graph (for 2012, the first year)
    scales = scale(start_w, end_w, start_h, end_h);
    drawScatter(converted_data, scales[0], scales[1], scales[2], year);

    // allow interaction by letting the user choose the year of data
    document.getElementById("Year").onclick = function() {
      d3.selectAll("svg").remove()
      drawScatter(converted_data, scales[0], scales[1], scales[2], document.getElementById("Year").value);
    };

  }).catch(function(e){
      throw(e);
  });

};

function convert(teenViolentData, teenPregData, dataGDP) {

  var converted_data = {};

  // add years
  for (i = startyear; i < endyear + 1; i++) {
    converted_data[i] = [];

    for (var country in teenViolentData) {
      if (country != 'OECD - Average') {
        // parse teen violence data
        var teenViol = 0;
        teenViolentData[country].forEach(function(d) {
          if (d['Time'] == i) {
            teenViol = d['Datapoint'];
          };
        });

        // parse teen pregnancy data
        var teenPreg = 0;
        if (country in teenPregData) {
          teenPregData[country].forEach(function(d) {
            if (d['Time'] == i) {
              teenPreg = d['Datapoint'];
            };
          });
        };

        // parse GDP data
        var gdp = 0;
        if (country in dataGDP) {
          dataGDP[country].forEach(function(d) {
            if (d['Year'] == i) {
              gdp = d['Datapoint'];
            };
          });
        };

        // put data into dictionary
        converted_data[i].push({
          'Country': country,
          'teenViol': teenViol,
          'teenPreg': teenPreg,
          'gdp': gdp
        });
      };
    };
  };
  return converted_data;
};


function transformResponse(data){

    // Save data
    let originalData = data;

    // access data property of the response
    let dataHere = data.dataSets[0].series;

    // access variables in the response and save length for later
    let series = data.structure.dimensions.series;
    let seriesLength = series.length;

    // set up array of variables and array of lengths
    let varArray = [];
    let lenArray = [];

    series.forEach(function(serie){
        varArray.push(serie);
        lenArray.push(serie.values.length);
    });

    // get the time periods in the dataset
    let observation = data.structure.dimensions.observation[0];

    // add time periods to the variables, but since it's not included in the
    // 0:0:0 format it's not included in the array of lengths
    varArray.push(observation);

    // create array with all possible combinations of the 0:0:0 format
    let strings = Object.keys(dataHere);

    // set up output object, an object with each country being a key and an array
    // as value
    let dataObject = {};

    // for each string that we created
    strings.forEach(function(string){
        // for each observation and its index
        observation.values.forEach(function(obs, index){
            let data = dataHere[string].observations[index];
            if (data != undefined){

                // set up temporary object
                let tempObj = {};

                let tempString = string.split(":").slice(0, -1);
                tempString.forEach(function(s, indexi){
                    tempObj[varArray[indexi].name] = varArray[indexi].values[s].name;
                });

                // every datapoint has a time and ofcourse a datapoint
                tempObj["Time"] = obs.name;
                tempObj["Datapoint"] = data[0];
                tempObj["Indicator"] = originalData.structure.dimensions.series[1].values[0].name;

                // Add to total object
                if (dataObject[tempObj["Country"]] == undefined){
                  dataObject[tempObj["Country"]] = [tempObj];
                } else {
                  dataObject[tempObj["Country"]].push(tempObj);
                };
            }
        });
    });

    // return the finished product!
    return dataObject;
}

/********
 * Transforms response of OECD request for GDP.
 * https://stats.oecd.org/SDMX-JSON/data/SNA_TABLE1/AUS+AUT+BEL+CAN+CHL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EU28+EU15+OECDE+OECD+OTF+NMEC+ARG+BRA+BGR+CHN+COL+CRI+HRV+CYP+IND+IDN+MLT+ROU+RUS+SAU+ZAF+FRME+DEW.B1_GE.HCPC/all?startTime=2012&endTime=2018&dimensionAtObservation=allDimensions
 **/

function transformResponseGDP(data){

    // Save data
    let originalData = data;

    // access data
    let dataHere = data.dataSets[0].observations;

    // access variables in the response and save length for later
    let series = data.structure.dimensions.observation;
    let seriesLength = series.length;

    // get the time periods in the dataset
    let observation = data.structure.dimensions.observation[0];

    // set up array of variables and array of lengths
    let varArray = [];
    let lenArray = [];

    series.forEach(function(serie){
        varArray.push(serie);
        lenArray.push(serie.values.length);
    });

    // add time periods to the variables, but since it's not included in the
    // 0:0:0 format it's not included in the array of lengths
    varArray.push(observation);

    // create array with all possible combinations of the 0:0:0 format
    let strings = Object.keys(dataHere);

    // set up output array, an array of objects, each containing a single datapoint
    // and the descriptors for that datapoint
    let dataObject = {};

    // for each string that we created
    strings.forEach(function(string){
        observation.values.forEach(function(obs, index){
            let data = dataHere[string];
            if (data != undefined){

                // set up temporary object
                let tempObj = {};

                // split string into array of elements seperated by ':'
                let tempString = string.split(":")
                tempString.forEach(function(s, index){
                    tempObj[varArray[index].name] = varArray[index].values[s].name;
                });

                tempObj["Datapoint"] = data[0];

                // Add to total object
                if (dataObject[tempObj["Country"]] == undefined){
                  dataObject[tempObj["Country"]] = [tempObj];
                } else if (dataObject[tempObj["Country"]][dataObject[tempObj["Country"]].length - 1]["Year"] != tempObj["Year"]) {
                    dataObject[tempObj["Country"]].push(tempObj);
                };

            }
        });
    });

    // return the finished product!
    return dataObject;
}


function scale(start_w, end_w, start_h, end_h) {
  // sets the scale for the x-axis
  var xScale = d3.scaleLinear()
                 .domain([0, end_x])
                 .range([start_w, end_w]);

  // sets the scale for the y-axis
  var yScale = d3.scaleLinear()
                 .domain([end_y, 0])
                 .range([start_h, end_h - start_h]);

  var colorScale = d3.scaleThreshold()
                     .domain([20000, 30000, 45000, 60000])
                     .range(colors);

  return [xScale, yScale, colorScale];
}

function drawScatter(data, xScale, yScale, colorScale, year) {

  // initiate the axes
  var xAxis = d3.axisBottom(xScale);
  var yAxis = d3.axisLeft(yScale);

  // draw the svg
  var svg = d3.select("body")
              .append("svg")
              .attr("width", w)
              .attr("height", h);

  // draw both axes
  svg.append("g")
     .attr("transform", "translate(0, "+ end_h +")")
     .call(xAxis);

  svg.append("g")
     .attr("transform", "translate("+ start_w +", "+ start_h +")")
     .call(yAxis);

  var tip = d3.tip()
     .attr('class', 'd3-tip')
     .offset([-10, 0])
     .html(function(d) {
       return "<strong>" + d["Country"] + "</strong>, GDP: $" + Math.round(d["gdp"]);
   });

  svg.call(tip);

  // draw the data points
  svg.selectAll("circle")
     .data(data[year])
     .enter()
     .append("circle")
     .attr("class", "dot")
     .attr("cx", function (d) {
       return xScale(d['teenViol'])
     })
     .attr("cy", function(d) {
       return yScale(d['teenPreg']);
     })
     .attr("r", 5)
     .attr('fill', function(d) {
       return colorScale(d['gdp'])
     })
     .on('mouseover', tip.show)
     .on('mouseout', tip.hide);

  // set graph title
  svg.append("text")
     .attr("x", w/2)
     .attr("y", start_h)
     .attr("font-family", "arial")
     .attr("font-weight", "bold")
     .attr("text-anchor", "middle")
     .text("Teens violence and teen pregnancies in OECD countries");

  // set graph description
  svg.append("text")
     .attr("x", start_w - 40)
     .attr("y", 2*start_h - 20)
     .attr("font-family", "arial")
     .attr("margin-left", "30px")
     .text("This graph shows the percentage of teens experiencing violence, teen pregnancies and GDP per capita for OECD countries.");

  // set axis titles
  svg.append("text")
     .attr("x", w/2 - 2*start_w)
     .attr("y", h - start_h)
     .attr("font-family", "arial")
     .text("Teens that experience violence (%)");

  svg.append("text")
     .attr("x", -end_h/2)
     .attr("y", start_w/2)
     .attr("text-anchor", "middle")
     .attr("transform", "rotate(-90)")
     .attr("font-family", "arial")
     .text("Teen pregnancy (%)");

  // make legend
  var categories = ['< 20000', '20000-30000', '30000-45000', '45000 >'];
  var leg_y = 130;

  for (i = 0; i < 4; i++) {
    svg.append("circle")
       .attr("cx", w - 2*start_w)
       .attr("cy", leg_y)
       .attr("r", 5)
       .style("fill", colors[i]);

    svg.append("text")
       .attr("x", w - 2*start_w + 20)
       .attr("y", leg_y)
       .text(categories[i])
       .attr("font-family", "arial")
       .style("font-size", "15px")
       .attr("alignment-baseline","middle");

       leg_y = leg_y + 30
  }

}
