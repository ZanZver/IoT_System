const mongoose = require("mongoose");

var addressSchema = new mongoose.Schema({
    addressLine1:{
        type: String
    },
    addressLine2:{
        type: String
    }
});

var loationSchema = new mongoose.Schema({
    Address: {
        type: addressSchema
    },
    Postcode:{
        type: String
    },
    City:{
        type: String
    },
    Country:{
        type: String
    }
});

var userSchema = new mongoose.Schema({
    Username:{
        type: String
    },
    Password:{
        type: String
    },
    Email:{
        type: String,
        required: "This field is required."
    },
    Name:{
        type: String,
        required: "This field is required."
    },
    Surname:{
        type: String
    },
    Loation: {
        type: loationSchema
    }
});

userSchema.path("Email").validate((val) => {
    emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return emailRegex.test(val);
}, "Invalid e-mail")

mongoose.model("User", userSchema);
//mongoose.model("User", userSchema2)