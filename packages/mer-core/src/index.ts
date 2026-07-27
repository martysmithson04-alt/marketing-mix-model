export {
  calculateMer,
  calculateBreakEvenMer,
  isAboveBreakEven,
  formatMer,
} from "./mer.js";

export {
  suggestAllocation,
  type AllocationChannelInput,
  type AllocationAction,
  type ChannelEfficiency,
  type SuggestAllocationInput,
  type SuggestAllocationResult,
} from "./allocation.js";

export {
  sumLinkClicks,
  computeClickShare,
  diagnoseTraffic,
  type TrafficChannelInput,
  type ClickShareRow,
  type TrafficDiagnosticsInput,
  type TrafficDiagnosticsResult,
} from "./traffic.js";
