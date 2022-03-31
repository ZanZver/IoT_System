const mongoose = require("mongoose");

// mongodb://localhost:30028/TestDB?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false
// mongodb://localhost:30028/TestDB?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false
var DB_engine = "mongodb://";
var DB_domain = "localhost";
var DB_port = ":30028";
var DB_database = "/TestDB";
var DB_readPreference = "?readPreference=primary";
var DB_appname = "&appname=MongoDB";
var DB_Compass_direct_Connection= "%20Compass&directConnection=true";
var DB_ssl = "&ssl=false";

console.log(DB_engine+DB_domain+DB_port+DB_database+DB_readPreference+DB_appname+DB_Compass_direct_Connection+DB_ssl)

mongoose.connect(DB_engine+DB_domain+DB_port+DB_database+DB_readPreference+DB_appname+DB_Compass_direct_Connection+DB_ssl, {useNewUrlParser: true}, (err) => {
    if(!err){
        console.log("MongoDB Conncetion Succeeded!")
    }
    else{
        console.log("Error in DB connection: " + err)
    }
});

require("./employee.model");
require("./user.model.js");