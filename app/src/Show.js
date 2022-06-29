import { useParams, Link } from "react-router-dom";
import { useQuery } from "react-query";
import { getShowById } from "./api";

function App() {
  const params = useParams();

  const data = useQuery({
    queryFn: () => getShowById(params.showId),
    queryKey: params.showId,
  });

  if (!data || !data.data || !data.data || data.isLoading) {
    return <span>Fetching show ID: {params.showId}</span>;
  }

  return (
    <div className="App">
      <h3 className="text-2xl mb-4">Show id: {params.showId}</h3>

      <div className="mb-8">
        <Link className="p-2 bg-gray-200 rounded" to={`/app/`}>
          Back to search
        </Link>
      </div>

      {Object.keys(data.data).map((key) => (
        <p key={key} className="mb-2">
          <span className="font-medium">{key}</span>:{" "}
          <span>{data.data[key]}</span>
        </p>
      ))}
    </div>
  );
}

export default App;
