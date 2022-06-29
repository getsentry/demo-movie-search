import { useState } from "react";
import { useQuery } from "react-query";
import { getShows } from "./api";
import { Link } from "react-router-dom";

const List = ({ query }) => {
  const data = useQuery({
    queryFn: () => getShows(query),
    queryKey: query,
    enabled: !!query,
  });

  if (!query) {
    return null;
  }

  if (!data || !data.data || !data.data.results || data.isLoading) {
    return <span>Searching for: {query}</span>;
  }

  return (
    <div>
      <h3 className="text-2xl mb-2">All shows:</h3>
      <ol className="list-decimal">
        {data.data.results.length ? (
          data.data.results?.map((show, index) => (
            <li key={show.pk}>
              <Link
                className="hover:text-gray-500"
                to={`/app/shows/${show.pk}`}
              >
                {show.title}
              </Link>
            </li>
          ))
        ) : (
          <li>No results</li>
        )}
      </ol>
    </div>
  );
};

function App() {
  const [input, setInput] = useState("");
  const [query, setQuery] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    setQuery(input);
  };

  return (
    <div className="App">
      <h1 className="text-3xl mb-4">Shows</h1>
      <div>
        <div className="w-full max-w-xs">
          <form className="mb-4" onSubmit={handleSubmit}>
            <div className="mb-4">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="show"
              >
                Enter name of the show
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="show"
                type="text"
                placeholder="Show name"
                onChange={(e) => setInput(e.target.value)}
                value={input}
              />
            </div>

            <div className="flex items-center justify-between">
              <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit"
              >
                Search
              </button>
            </div>
          </form>
        </div>
      </div>

      <List query={query} />
    </div>
  );
}

export default App;
