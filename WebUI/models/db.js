const mongoose = require("mongoose");

var DB_engine = "mongodb://";
var DB_domain = "localhost";
var DB_port = ":27019";
var DB_database = "/initialDB";
var DB_options = "?directConnection=true&serverSelectionTimeoutMS=2000";
var DB_appname = "&appName=mongosh+1.3.0";

mongoose.connect(DB_engine+DB_domain+DB_port+DB_database+DB_options+DB_appname, {useNewUrlParser: true}, (err) => {
    if(!err){
        console.log("MongoDB Conncetion Succeeded!")
    }
    else{
        console.log("Error in DB connection: " + err)
    }
});

require("./employee.model");
require("./user.model.js");