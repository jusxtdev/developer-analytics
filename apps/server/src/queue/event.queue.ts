import { batchInput, eventInput } from "@/schemas/eventBatch.schema.js";
import { AppError } from "@/utils/appError.js";
import { Queue } from "bullmq";
import { redisConnection } from "../config/redis.js";

export const batchQueue = new Queue("batch-queue", {
  connection: redisConnection,
});

export async function addEventsToQueue(batch: batchInput) {
  const job = batch.map((event: eventInput) => ({
    name: "batch-queue",
    data: event,
  }));
  try {
    await batchQueue.addBulk(job);
  } catch (err) {
    console.error(err);
    throw AppError.internal();
  }
}
