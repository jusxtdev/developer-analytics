import { env } from "@/env.js";
import { Response, type CookieOptions } from "express";

const isProduction = env.NODE_ENV === "production";

const isHTTPSrequest = (res?: Response) => {
  res?.req.secure || res?.req.headers["x-forwarded-proto"] === "https";
};

export const getAuthOptions = (res?: Response): CookieOptions => {
  const needsCrossSiteCookie = isProduction || isHTTPSrequest(res);

  return {
    httpOnly: true,
    secure: needsCrossSiteCookie!,
    sameSite: needsCrossSiteCookie ? "none" : "lax",
  };
};

export default async function storeCookie(
  title: string,
  data: any,
  res: Response,
) {
  res.cookie(title, data, {
    ...getAuthOptions(res),
    maxAge: 1000 * 60 * 60 * 24 * 7,
  });
}
