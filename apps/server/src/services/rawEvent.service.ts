import { prisma } from "@/config/db.js";
import { eventInput } from "@/schemas/eventBatch.schema.js";

const addEvent = async (event : eventInput) => {
    try {
        await prisma.rawEvents.create({
            data : {
                userId : 1,
                timestamp : event.timestamp,
                window_title : event.title,
                application : event.application,
                isIdle : event.isIdle
            }
        })
    } catch (error) {
        console.error(error)
    }
}

const RawEventService = {
    addEvent
}
export default RawEventService