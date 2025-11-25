const Event = require('../models/Event');

/**
 * Registers the current authenticated user for a specific event,
 * validating against capacity and approval status.
 */
exports.registerEvent = async (req, res) => {
  try {
    // We use findByIdAndUpdate with MongoDB $addToSet and $push, 
    // but the following approach is safer for capacity check.
    
    const event = await Event.findById(req.params.id);
    
    if (!event) {
      return res.status(404).json({ message: 'Event not found' });
    }
    
    // Check if the event is approved by an admin
    if (event.status !== 'approved') {
      return res.status(400).json({ message: 'Event is not yet approved and cannot accept registrations.' });
    }
    
    // Check Capacity
    if (event.attendees.length >= event.capacity) {
      return res.status(400).json({ message: 'Event is fully booked. Registration failed.' });
    }

    // Check if user is already registered
    if (event.attendees.includes(req.user._id)) {
      return res.status(400).json({ message: 'You are already registered for this event.' });
    }

    // Add user to attendees array
    event.attendees.push(req.user._id);
    await event.save();
    
    res.json({ 
        message: 'Registration successful!',
        eventTitle: event.title 
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

/**
 * Removes the current authenticated user from an event's attendee list.
 */
exports.cancelRegistration = async (req, res) => {
  try {
    const event = await Event.findById(req.params.id);
    
    if (!event) {
      return res.status(404).json({ message: 'Event not found' });
    }

    // Filter the current user out of the attendees array
    const initialAttendeeCount = event.attendees.length;

    event.attendees = event.attendees.filter(
      (userId) => userId.toString() !== req.user._id.toString()
    );

    // Check if a registration was actually removed
    if (event.attendees.length === initialAttendeeCount) {
        return res.status(404).json({ message: 'Registration not found. You were not registered for this event.' });
    }
    
    await event.save();
    
    res.json({ message: 'Registration successfully cancelled.' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};