//@ts-check
import axios from "axios";
import * as Sentry from "@sentry/react";

export const getShows = async (query) => {
  if (!query) {
    const transaction = Sentry.startTransaction({ name: "/api/shows" });
    const response = await axios.get("/api/shows/");
    transaction.finish();
    return response.data;
  }

  const transaction = Sentry.startTransaction({
    name: `/api/shows/?q=${query}`,
  });

  const response = await axios.get(`/api/shows/?q=${query}`);
  transaction.finish();
  return response.data;
};

export const getShowById = async (showId) => {
  const transaction = Sentry.startTransaction({ name: `/api/shows/${showId}` });
  const response = await axios.get(`/api/shows/${showId}`);
  transaction.finish();
  return response.data;
};
