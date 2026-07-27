import { z } from "zod";

export const IsoDateString = z
  .string()
  .regex(/^\d{4}-\d{2}-\d{2}$/, "Expected YYYY-MM-DD");

export const MerQuerySchema = z.object({
  from: IsoDateString,
  to: IsoDateString,
  includeAllocation: z.coerce.boolean().optional().default(true),
});

export const ChannelMerSchema = z.object({
  name: z.string(),
  spend: z.number().nonnegative(),
  salesContribution: z.number().nonnegative().optional(),
  effectiveMer: z.number().nullable().optional(),
  spendShare: z.number().min(0).max(1).optional(),
});

export const AllocationActionSchema = z.object({
  type: z.enum(["cut", "shift", "hold", "watch"]),
  channel: z.string(),
  percentChange: z.number().optional(),
  detail: z.string(),
});

export const AllocationSuggestionSchema = z.object({
  suggestedTestDays: z.number().int().positive(),
  why: z.string(),
  actions: z.array(AllocationActionSchema),
  isAboveBreakEven: z.boolean().nullable(),
});

export const MerResponseSchema = z.object({
  from: IsoDateString,
  to: IsoDateString,
  sales: z.number().nonnegative(),
  spend: z.number().nonnegative(),
  mer: z.number().nullable(),
  breakEvenMer: z.number().positive(),
  channels: z.array(ChannelMerSchema),
  allocation: AllocationSuggestionSchema.optional(),
});

export const ManualSpendEntrySchema = z.object({
  date: IsoDateString,
  channel: z.string().min(1),
  amount: z.number().nonnegative(),
  currency: z.string().length(3).default("USD"),
});

export const PostSpendBodySchema = z.object({
  entries: z.array(ManualSpendEntrySchema).min(1),
});

export const PostSpendResponseSchema = z.object({
  accepted: z.number().int().nonnegative(),
  shopId: z.string(),
});

export const AllocationQuerySchema = z.object({
  from: IsoDateString,
  to: IsoDateString,
});

export const AllocationResponseSchema = z.object({
  from: IsoDateString,
  to: IsoDateString,
  breakEvenMer: z.number().positive(),
  overallMer: z.number().nullable(),
  allocation: AllocationSuggestionSchema,
  channels: z.array(ChannelMerSchema),
});

export const ErrorResponseSchema = z.object({
  error: z.string(),
  code: z.string().optional(),
});

export const TrafficQuerySchema = z.object({
  from: IsoDateString,
  to: IsoDateString,
});

export const ClickShareRowSchema = z.object({
  name: z.string(),
  linkClicks: z.number().nonnegative(),
  clickShare: z.number().min(0).max(1),
});

export const TrafficResponseSchema = z.object({
  from: IsoDateString,
  to: IsoDateString,
  sessions: z.number().nonnegative(),
  totalPaidLinkClicks: z.number().nonnegative(),
  estimatedOrganicSessions: z.number().nonnegative(),
  estimatedOrganicShare: z.number().min(0).max(1).nullable(),
  estimatedPaidShare: z.number().nonnegative().nullable(),
  paidClicksExceedSessions: z.boolean(),
  clickShare: z.array(ClickShareRowSchema),
  assumptions: z.array(z.string()),
  why: z.string(),
});

export const ManualLinkClickEntrySchema = z.object({
  date: IsoDateString,
  channel: z.string().min(1),
  clicks: z.number().int().nonnegative(),
});

export const ManualSessionEntrySchema = z.object({
  date: IsoDateString,
  sessions: z.number().int().nonnegative(),
});

export const PostTrafficBodySchema = z
  .object({
    linkClicks: z.array(ManualLinkClickEntrySchema).optional(),
    sessions: z.array(ManualSessionEntrySchema).optional(),
  })
  .refine(
    (body) =>
      (body.linkClicks?.length ?? 0) > 0 || (body.sessions?.length ?? 0) > 0,
    { message: "Provide at least one linkClicks or sessions entry" },
  );

export const PostTrafficResponseSchema = z.object({
  acceptedLinkClicks: z.number().int().nonnegative(),
  acceptedSessions: z.number().int().nonnegative(),
  shopId: z.string(),
});

export type MerQuery = z.infer<typeof MerQuerySchema>;
export type MerResponse = z.infer<typeof MerResponseSchema>;
export type PostSpendBody = z.infer<typeof PostSpendBodySchema>;
export type PostSpendResponse = z.infer<typeof PostSpendResponseSchema>;
export type AllocationQuery = z.infer<typeof AllocationQuerySchema>;
export type AllocationResponse = z.infer<typeof AllocationResponseSchema>;
export type TrafficQuery = z.infer<typeof TrafficQuerySchema>;
export type TrafficResponse = z.infer<typeof TrafficResponseSchema>;
export type PostTrafficBody = z.infer<typeof PostTrafficBodySchema>;
export type PostTrafficResponse = z.infer<typeof PostTrafficResponseSchema>;
