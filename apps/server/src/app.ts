import { config } from "dotenv";
import express, {Request, Response} from "express";
import { connectDB } from "./config/db.js";
import rootRouter from "./routes/root.router.js";
const app = express();

config();

await connectDB();

const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
// app.use(cookieParser());

app.use("/api", rootRouter);

// All route catcher for undefined routees
app.all("/{*splat}", (_req: Request, res: Response) => {
//   throw new AppError(`${req.method} ${req.originalUrl} Not found`, 404);
    res.status(404).send("Not implemented")
});

// gloabal error handler
// app.use(errorHandler);

export { app, PORT };