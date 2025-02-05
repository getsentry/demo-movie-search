import * as Sentry from "@sentry/react";
import React from "react";
import ReactDOM from "react-dom/client";
import { QueryClient, QueryClientProvider } from "react-query";
import {
  createRoutesFromChildren,
  matchRoutes,
  useLocation,
  useNavigationType,
  BrowserRouter,
  Route,
  Routes,
} from "react-router-dom";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import Show from "./Show";
import Shows from "./Shows";

const SentryRoutes = Sentry.withSentryReactRouterV6Routing(Routes);

const sentrySpotlight = process.env.SENTRY_SPOTLIGHT || true;
const sentryDsn = process.env.REACT_APP_SENTRY_DSN;
const sentryRelease = process.env.REACT_APP_SENTRY_RELEASE || "0.0.1";
const sentryEnvironment = process.env.REACT_APP_SENTRY_ENVIRONMENT || "dev";
const sentryTracesSampleRate = Number.parseFloat(
  process.env.REACT_APP_SENTRY_TRACES_SAMPLE_RATE || "1.0"
);
const sentryDebug = process.env.REACT_APP_SENTRY_DEBUG_FRONTEND || true;
const serverSide = process.env.REACT_APP_SERVER_SIDE || false;

console.log("~~~~ sentrySpotlight: ", sentrySpotlight);
console.log("~~~~ sentryDsn: ", sentryDsn);
console.log("~~~~ sentryRelease: ", sentryRelease);
console.log("~~~~ sentryEnvironment: ", sentryEnvironment);
console.log("~~~~ sentryTracesSampleRate: ", sentryTracesSampleRate);
console.log("~~~~ sentryDebug: ", sentryDebug);
console.log("~~~~ serverSide: ", serverSide);

const integrations = [
  Sentry.reactRouterV6BrowserTracingIntegration({
    useEffect: React.useEffect,
    useLocation,
    useNavigationType,
    createRoutesFromChildren,
    matchRoutes,
  }),
];

if (sentrySpotlight) {
  const sidecarUrl =
    typeof sentrySpotlight === "string" ? sentrySpotlight : undefined;
  integrations.push(
    Sentry.spotlightBrowserIntegration({
      sidecarUrl,
    })
  );
}

Sentry.init({
  dsn: sentryDsn,
  integrations,
  release: sentryRelease,
  environment: sentryEnvironment,
  tracesSampleRate: sentryTracesSampleRate,
  debug: sentryDebug,
  tracePropagationTargets: ["localhost", /^\//],
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
      <BrowserRouter basename={`${serverSide ? "/server_side" : "/"}`}>
        <SentryRoutes>
          <Route path="/app" element={<Shows />} />
          <Route path="/app/shows/:showId" element={<Show />} />
        </SentryRoutes>
      </BrowserRouter>
    </div>
  </QueryClientProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
