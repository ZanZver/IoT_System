const mongoose = require("mongoose");

var userSchema = new mongoose.Schema({
    username:{
        type: String
    },
    email:{
        type: String,
        required: "This field is required."
    },
    password:{
        type: String
    },
    name:{
        type: String,
        required: "This field is required."
    },
    surname:{
        type: String
    },
    addressLine1:{
        type: String
    },
    addressLine2:{
        type: String
    },
    postcode:{
        type: String
    },
    city:{
        type: String
    },
    country:{
        type: String
        
    }
});

var addressSchema = new mongoose.Schema({
    addressLine1:{
        type: String
    },
    addressLine2:{
        type: String
    },
});

var userSchema2 = new mongoose.Schema({
    username:{
        type: String
    },
    email:{
        type: String,
        required: "This field is required."
    },
    password:{
        type: String
    },
    name:{
        type: String,
        required: "This field is required."
    },
    surname:{
        type: String
    },
    
    address: [addressSchema],

    postcode:{
        type: String
    },
    city:{
        type: String
    },
    country:{
        type: String
        
    }
});

userSchema.path("email").validate((val) => {
    emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return emailRegex.test(val);
}, "Invalid e-mail")

mongoose.model("User", userSchema);