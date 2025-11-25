const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const UserSchema = new mongoose.Schema({
  username: { type: String, required: true },
  email:    { type: String, required: true, unique: true },
  password: { type: String, required: true },
  role:     { type: String, enum: ['user', 'admin'], default: 'user' }
});

// 🔑 CORRECTED HOOK: Using async/await requires omitting the 'next' argument 
// and relying on Mongoose to wait for the promise to resolve.
UserSchema.pre('save', async function() {
  // If password field is not modified, skip hashing and return.
  if (!this.isModified('password')) return; 
  
  const salt = await bcrypt.genSalt(10);
  this.password = await bcrypt.hash(this.password, salt);
});

module.exports = mongoose.model('User', UserSchema);