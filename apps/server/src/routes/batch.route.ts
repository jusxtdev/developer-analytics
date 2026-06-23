import BatchController from "@/controller/batch.controller.js";
import { validate } from "@/middleware/validate.middleware.js";
import EventBatchSchema from "@/schemas/eventBatch.schema.js";
import express from "express";

const router = express.Router();

router.post("/", validate(EventBatchSchema.batch), BatchController.newBatch);

export default router;
