import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/videos/';

// Get videos for the current user (max 3) 
export async function getVideos(token) {
  try {
    const res = await axios.get(`${API_BASE}presentations/`, {
      headers: { Authorization: `Token ${token}` }
    });
    return res.data;
  } catch (error) {
    throw 'error get videos';
  }
}

// Upload a new video
export async function uploadVideo(file, token) {
  try {
    const formData = new FormData();
    formData.append('video', file);
    const res = await axios.post(`${API_BASE}presentations/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Token ${token}`
      }
    });
    return res.data;
  } catch (error ) {
    throw 'error upload' ;
  }
}

// Delete a video by ID
export async function deleteVideo(id, token) {
  try {
    await axios.delete(`${API_BASE}presentations/${id}/`, {
      headers: { Authorization: `Token ${token}` }
    });
  } catch (error) {
    throw 'error delete video';
  }
}

// Set a video as official (final_validated)
export async function setOfficialVideo(id, token) {
  try {
    const res = await axios.patch(
      `${API_BASE}presentations/${id}/`,
      { final_validated: true },
      { headers: { Authorization: `Token ${token}` } }
    );
    return res.data;
  } catch (error) {
    throw 'error set official video';
  }
}

// Update video details (PATCH)
export async function updateVideo(id, data, token) {
  try {
    const res = await axios.patch(
      `${API_BASE}presentations/${id}/`,
      data,
      { headers: { Authorization: `Token ${token}` } }
    );
    return res.data;
  } catch (error) {
    throw 'error update video';
  }
}
