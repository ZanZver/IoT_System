//.lean()
const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');

const User = mongoose.model('User');
const Employee = mongoose.model('Employee');
const IoT_Customer_Device = mongoose.model("IoT_Customer_Device");

function updateRecord(req, res) {
    var userKeyID = "62786354667fe8741957fb2d";
    IoT_Customer_Device.findOneAndUpdate(
        { UserID: userKeyID }, 
        [{$set:req.body}], 
        { new: true }, 
        (err, doc) => {
        if (!err) { res.redirect('/devices/smart_light'); }
        (err, doc) => {
            if (!err) { res.redirect('/devices/smart_light'); }
            else {
                if (err.name == 'ValidationError') {
                    handleValidationError(err, req.body);
                    res.render("devices/edit_smart_light", {
                        viewTitle: "Update smart light",
                        device_smart_light: data.smart_light[req.body.Device_ID]
                    });
                }
                else
                    console.log('Error during record update : ' + err);
            }
        }
    }).lean();
}

router.get('/', (req, res) => {
    let userKeyID =  "62786354667fe8741957fb2d";
    IoT_Customer_Device.aggregate([
        {$match: {UserID:userKeyID}},
        {$project: {
            _id:0,UserID:0
        }}
    ]).exec((err, docs) => {
        res.render("devices/smart_light", {
            list: docs[0].smart_light
        });
    });
});

router.post('/', (req, res) => {
    if (req.body._id == ''){
        console.log("Naah");
    }    
    else{
        updateRecord(req, res);   
    }
        
});

router.get('/edit/:id', (req, res) => {
    itemId = req.params.id;
    userKeyID = "62786354667fe8741957fb2d";
    IoT_Customer_Device.findOne(
        {UserID: userKeyID},
        {"_id":0}
        ).lean().exec(function (err, data) {
            if (!err) {
                res.render("devices/edit_smart_light", {
                    viewTitle: "Update smart light",
                    device_smart_light: data.smart_light[itemId]
                });
            }
            else { console.log('Error in device edit :' + err); };
        }
        );
});

router.get('/delete/:id', (req, res) => {
    let userKeyID =  "62786354667fe8741957fb2d";
    let removeLoc = "smart_light.";
    removeLoc += req.params.id;

    IoT_Customer_Device.updateOne(
        { UserID: userKeyID },
        [{ $unset: removeLoc }],
        (err, data) => {
            if (!err) {
                res.redirect('/devices/smart_light');
            }
            else { console.log('Error in device delete :' + err); }
        }
    );
});
module.exports = router;