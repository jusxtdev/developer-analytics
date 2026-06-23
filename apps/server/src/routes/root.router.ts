import express, { Request, Response } from "express";
import batchRoter from "./batch.route.js"

const router = express.Router();

router.get("/", (_req: Request, res: Response) => {
  res.json({ message: "Welcome to the Developer Analytics API" });
});

router.use("/event/batch", batchRoter)

export default router;
