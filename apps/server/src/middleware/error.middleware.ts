import { env } from "@/env.js";
import { AppError } from "@/utils/appError.js";
import { Request, Response, NextFunction } from "express";

export const errorHandler = (
  err: Error,
  _req: Request,
  res: Response,
  _next: NextFunction,
) => {
  if (err instanceof AppError){
    return res.status(err.statusCode).json({
        status : err.status,
        msg : err.message,
    })
  }

  // unhandled errors
  console.error("Unhandled Error ", err)

  res.status(500).json({
    status : false,
    msg : env.NODE_ENV === "production" ? "Internal Server Error" : err.message
  })
};