const mongoose = require("mongoose");

var devicesSchema = new mongoose.Schema({
    Smart_light:{},
    Smart_fridge:{},
    Smart_vacuum:{}
});

var IoT_Customer_Device = new mongoose.Schema({
    UserID: {
        type: String
    },
    Smart_light:{},
    Smart_fridge:{},
    Smart_vacuum:{}
},{
    writeConcern: {
      w: 'majority',
      j: true,
      wtimeout: 1000
    }});

mongoose.model("IoT_Customer_Device", IoT_Customer_Device);