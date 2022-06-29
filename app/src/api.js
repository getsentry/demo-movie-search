import axios from "axios";

export const getShows = async (query) => {
  if (!query) {
    const response = await axios.get("/api/shows/");
    return response.data;
  }

  const response = await axios.get(`/api/shows/?q=${query}`);
  return response.data;
};

export const getShowById = async (showId) => {
  const response = await axios.get(`/api/shows/${showId}`);
  return response.data;
};
