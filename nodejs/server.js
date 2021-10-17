// https://stackoverflow.com/questions/26049013/node-js-get-number-of-processors-available/37871843
// https://stackoverflow.com/questions/28705009/how-do-i-get-the-server-uptime-in-node-js/28706630
// https://github.com/nodejs/help/issues/1140
// https://github.com/uc-botheaj/it3038c-script-notes/tree/main/Week6
//
// Script was adapted from the sources above to serve the following purpose:
// -Spins up a simple webpage to display a homepage and system info.
// -Lab 6 for IT3038c
// -To learn more nodejs (which I did)
//
//To run, install nodejs and ip then navigate to the directory that this script lives in and type "node server.js" then navigate to your browser and type localhost:3000
//Thanks for another cool project Prof Bothe



var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

String.prototype.toHHMMSS = function () {
    var sec_num = parseInt(this, 10); 
    var hours   = Math.floor(sec_num / 3600);
    var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
    var seconds = sec_num - (hours * 3600) - (minutes * 60);

    if (hours   < 10) {hours   = "0"+hours;}
    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}
    var time    = hours+':'+minutes+':'+seconds;
    return time;
}


const totalRAM = os.totalmem();
var totalRAMConverted = totalRAM / (1024 * 1024);
const freeRAM = os.freemem();
var availableRAM = freeRAM / (1024 * 1024);
var time = os.uptime();
var uptime = (time + "").toHHMMSS();
const cpuCount = os.cpus().length


http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${uptime} </p>
            <p>Total Memory: ${totalRAMConverted} </p>
            <p>Free Memory: ${availableRAM} </p>
            <p>Number of CPUs: ${cpuCount} </p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
