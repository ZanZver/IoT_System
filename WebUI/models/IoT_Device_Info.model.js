const mongoose = require("mongoose");


var IoT_Device_InfoSchema = new mongoose.Schema({
    Smart_light:{},
    Smart_fridge:{},
    Smart_vacuum:{}
},{
  collection: "iot_device_info",
  writeConcern: {
    w: 'majority',
    j: true,
    wtimeout: 1000
  }});

mongoose.model("IoT_Device_Info", IoT_Device_InfoSchema);