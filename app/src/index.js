import * as Sentry from "@sentry/react";
import { BrowserTracing } from "@sentry/tracing";
import ReactDOM from "react-dom/client";
import { QueryClient, QueryClientProvider } from "react-query";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import Show from "./Show";
import Shows from "./Shows";
import { createBrowserHistory } from "history";

const history = createBrowserHistory();

Sentry.init({
  dsn: process.env.REACT_APP_SENTRY_DSN,
  integrations: [
    new BrowserTracing({
      tracingOrigins: ["localhost", /^\//],
      routingInstrumentation: Sentry.reactRouterV6Instrumentation(history),
    }),
  ],
  release: process.env.REACT_APP_SENTRY_RELEASE,
  environment: process.env.REACT_APP_SENTRY_ENVIRONMENT,
  tracesSampleRate: 1.0,
  debug: true,
});

// Just a random new user, each time the page is reloaded
const userId = String(Math.floor(Math.random() * 1_000_000));
const userSegmentNumber = String(Math.floor(Math.random() * 1_000_000));

Sentry.setUser({
  id: userId,
  username: `Some user (${userId})}`,
  segment: `Some segment (${userSegmentNumber})}`,
});

const root = ReactDOM.createRoot(document.getElementById("root"));
const queryClient = new QueryClient();

root.render(
  <QueryClientProvider client={queryClient}>
    <div className="container mx-auto p-4">
      <BrowserRouter>
        <Routes>
          <Route path="/app" element={<Shows />} />
          <Route path="/app/shows/:showId" element={<Show />} />
        </Routes>
      </BrowserRouter>
    </div>
  </QueryClientProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
