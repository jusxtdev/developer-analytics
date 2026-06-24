import { logInInput, signUpInput } from "@/schemas/user.schema.js";
import UserService from "@/services/user.service.js";
import { ApiResponse } from "@/utils/apiResponse.js";
import { AppError } from "@/utils/appError.js";
import generateToken, { jwtPayload } from "@/utils/generateToken.js";
import storeCookie, { getAuthOptions } from "@/utils/storeCookie.js";
import bcrypt from "bcrypt";
import { Request, Response } from "express";

const signup = async (req: Request, res: Response) => {
  const body: signUpInput = req.body;

  const SALT = await bcrypt.genSalt(10);
  const hashedPass = await bcrypt.hash(body.password, SALT);

  const newUser = await UserService.signupUser(
    body.name,
    body.email,
    hashedPass,
  );

  const payload: jwtPayload = {
    userId: newUser.id,
    email: newUser.email,
  };
  const token = generateToken(payload);

  storeCookie("jwt", token, res);

  return ApiResponse.created(res, "Signup Successfull");
};

const login = async (req: Request, res: Response) => {
  const body: logInInput = req.body;

  const user = await UserService.findUserByEmail(body.email);
  if (!user) throw AppError.notFound("User not Found");

  const isValidPassword = await bcrypt.compare(body.password, user.password);
  if (!isValidPassword) throw new AppError("Invalid Password", 400, false);

  const payload: jwtPayload = {
    userId: user.id,
    email: user.email,
  };
  const token = generateToken(payload);
  storeCookie("jwt", token, res);

  return ApiResponse.ok(res, "Logged In successfully");
};

const logout = async (_req: Request, res: Response) => {
  res.clearCookie("jwt", getAuthOptions(res));
  return ApiResponse.ok(res, "Logged out");
};

const AuthController = { signup, login, logout };

export default AuthController;
