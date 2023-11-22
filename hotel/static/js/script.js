function trackActivity(hotelId, activityType) {
    console.log(`User visited Hotel ID ${hotelId}`);
 
    // Redirect based on activity type
    if (activityType === 'visit') {
        // Redirect to the hotel details page
        window.location.href = `/hotel_detail/${hotelId}/`;
    } else if (activityType === 'draft_booking') {
        // Redirect to the draft booking page
        window.location.href = `/draft_booking/${hotelId}/`;
    } else if (activityType === 'completed_booking') {
        // Redirect to the completed booking page
        window.location.href = `/completed_booking/${hotelId}/`;
    } else {
        // Default redirect, for example, back to the home page
        window.location.href = '/Home/';
    }
}


function makeDraftBooking(hotelId) {
    console.log(`User made a draft booking for Hotel ID ${hotelId}`);
    updateActivityList(`Draft Booking - Hotel ID ${hotelId}`);
}

function completeBooking(hotelId) {
    console.log(`User completed a booking for Hotel ID ${hotelId}`);
    updateActivityList(`Completed Booking - Hotel ID ${hotelId}`);
    updateRecommendationList(`Recommended Hotel - Hotel ID ${hotelId + 1}`);
}

function updateActivityList(activity) {
    const activityList = document.getElementById('activity-list');
    const listItem = document.createElement('li');
    listItem.textContent = activity;
    activityList.appendChild(listItem);
}

function updateRecommendationList(recommendation) {
    const recommendationList = document.getElementById('recommendation-list');
    const listItem = document.createElement('li');
    listItem.textContent = recommendation;
    recommendationList.appendChild(listItem);
}
