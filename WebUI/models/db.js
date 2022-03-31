const mongoose = require("mongoose");

// mongodb://localhost:30028/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false
mongoose.connect("mongodb://localhost:30028/TestDB?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false", {useNewUrlParser: true}, (err) => {
    if(!err){
        console.log("MongoDB Conncetion Succeeded!")
    }
    else{
        console.log("Error in DB connection: " + err)
    }
});

require("./employee.model");
require("./user.model.js");