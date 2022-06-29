import * as Sentry from "@sentry/react";
import { BrowserTracing } from "@sentry/tracing";
import ReactDOM from "react-dom/client";
import { QueryClient, QueryClientProvider } from "react-query";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import Show from "./Show";
import Shows from "./Shows";
import { createBrowserHistory } from 'history';

const history = createBrowserHistory();

Sentry.init({
  dsn: "https://4fa9b13665d74aa98c924d855fdddca0@o447951.ingest.sentry.io/6539773",
  integrations: [new BrowserTracing({
    tracingOrigins: ["localhost", "localhost:8000", "localhost:3000", /^\//],
    routingInstrumentation: Sentry.reactRouterV6Instrumentation(history),
  })],

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for performance monitoring.
  // We recommend adjusting this value in production
  tracesSampleRate: 1.0,
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
