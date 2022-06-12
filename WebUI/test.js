const mongoose = require("mongoose");


var DB_engine = "mongodb://";
var DB_domain = "localhost";
var DB_port = ":27020";
var DB_database = "/initialDB";
var DB_options = "?directConnection=true&serverSelectionTimeoutMS=2000";
var DB_appname = "&appName=mongosh+1.3.0";

//mongoose.connect('mongodb://mongosA:27501,mongosB:27501', cb);
mongoose.connect('mongodb://localhost:27019,localhost:27020,localhost:27021/initialDB', {useNewUrlParser: true}, (err) => {
    if(!err){
        console.log("MongoDB Conncetion Succeeded!")
    }
    else{
        console.log("Error in DB connection: " + err)
    }
});

var iot_device_info_schema = new mongoose.Schema({
    smart_light:{},
    smart_fridge:{},
    smart_vacuum:{}
    },
    { collection: "iot_device_info",
    
        writeConcern: {
          w: 'majority',
          j: true,
          wtimeout: 1000
        }});

var iot_device_info = mongoose.model('iot_device_info',iot_device_info_schema);

iot_device_info.find({})
    .exec(function (err,data) {
        console.log(err);
        console.log(data);
    });