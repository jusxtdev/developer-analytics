import cookieParser from "cookie-parser";
import { config } from "dotenv";
import express, { Request, Response } from "express";
import { connectDB } from "./config/db.js";
import { errorHandler } from "./middleware/error.middleware.js";
import rootRouter from "./routes/root.router.js";
import { AppError } from "./utils/appError.js";
const app = express();
config();

await connectDB();

const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

app.use("/api", rootRouter);

// All route catcher for undefined routees
app.all("/{*splat}", (_req: Request, _res: Response) => {
  //   throw new AppError(`${req.method} ${req.originalUrl} Not found`, 404);
  throw new AppError("Not Implemented", 404, false);
});

// gloabal error handler
app.use(errorHandler);

export { app, PORT };
