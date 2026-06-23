import { validate } from "@/middleware/validate.middleware.js";
import { addEventsToQueue } from "@/queue/event.queue.js";
import EventBatchSchema from "@/schemas/eventBatch.schema.js";
import express, { Request, Response } from "express";

const router = express.Router();

router.post(
  "/",
  validate(EventBatchSchema.batch),
  async (req: Request, res: Response) => {
    const batch = req.body
    try{
        await addEventsToQueue(batch)
    } catch (err) {
        console.error(err)
        res.status(500).json({
            msg : "Error occurred"
        })
    }
    console.log("Added to queue")
    res.status(200).json({
        msg : "Added to queue"
    })
  },
);

export default router;
