const mongoose = require('mongoose');

const EventSchema = new mongoose.Schema({
  title:       { type: String, required: true },
  description: { type: String },
  date:        { type: Date, required: true },
  time:        { type: String, required: true },
  location:    { type: String, required: true },
  capacity:    { type: Number, required: true },
  organizer:   { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  attendees:   [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }], // List of registered user IDs
  status:      { type: String, enum: ['pending', 'approved', 'rejected'], default: 'pending' }
}, { timestamps: true });

module.exports = mongoose.model('Event', EventSchema);