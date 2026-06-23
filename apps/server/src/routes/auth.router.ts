import AuthController from "@/controller/auth.controller.js";
import { validate } from "@/middleware/validate.middleware.js";
import UserSchema from "@/schemas/user.schema.js";
import express from "express";

const router = express.Router();

router.post("/", validate(UserSchema.createUser), AuthController.signup);

export default router;
