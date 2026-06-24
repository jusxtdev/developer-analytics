import AuthController from "@/controller/auth.controller.js";
import { validate } from "@/middleware/validate.middleware.js";
import UserSchema from "@/schemas/user.schema.js";
import express from "express";

const router = express.Router();

router.post("/signup", validate(UserSchema.signUp), AuthController.signup);

router.post("/login", validate(UserSchema.logIn), AuthController.login)

router.post("/logout", AuthController.logout)

export default router;
