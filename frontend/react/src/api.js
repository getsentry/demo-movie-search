//@ts-check
import axios from "axios";
import * as Sentry from "@sentry/react";

export const getShows = async (query) => {
  if (!query) {
    const response = await Sentry.startSpan(
      { name: "/api/shows", op: "http.get" },
      () => axios.get("/api/shows/")
    );
    return response.data;
  }

  const response = await Sentry.startSpan(
    {
      name: `/api/shows/?q=${query}`,
      op: "http.get",
    },
    () => axios.get(`/api/shows/?q=${query}`)
  );
  return response.data;
};

export const getShowById = async (showId) => {
  const response = await Sentry.startSpan(
    { name: `/api/shows/${showId}`, op: "http.get" },
    () => axios.get(`/api/shows/${showId}`)
  );
  return response.data;
};
