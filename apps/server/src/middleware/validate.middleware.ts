import { ZodSchema } from "zod";
import { Request, Response, NextFunction } from "express";

export const validate = (schema : ZodSchema) => {
    return async (req : Request, res : Response, next : NextFunction) => {
        const valid = schema.safeParse(req.body)
        if (!valid.success){
            const errorMessage = valid.error.issues
                    .map((issue) => issue.message)
                    .join(" | ");

            return res.status(411).json({
                "msg" : errorMessage
            })
        }
        next()
    }
}