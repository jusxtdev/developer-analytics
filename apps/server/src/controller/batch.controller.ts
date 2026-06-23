import { addEventsToQueue } from "@/queue/event.queue.js";
import { ApiResponse } from "@/utils/apiResponse.js";
import { Request, Response } from "express";

const newBatch = async (req: Request, res: Response) => {
  const batch = req.body;
  await addEventsToQueue(batch);
  console.log("Added Batch to queue");
  return ApiResponse.ok(res, "Added Batch to queue");
};

const BatchController = { newBatch };

export default BatchController;
