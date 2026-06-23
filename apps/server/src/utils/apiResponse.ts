import { Response } from "express";

export class ApiResponse {
  static send(res: Response, status: number, msg: string, data?: unknown) {
    return res.status(status).json({
      status: status < 400,
      msg,
      ...(data !== undefined && { data }),
    });
  }

  static ok(res: Response, message = "Success", data?: unknown) {
    return this.send(res, 200, message, data);
  }

  static created(res: Response, message = "Created", data?: unknown) {
    return this.send(res, 201, message, data);
  }
}
