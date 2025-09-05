-- summary.lua — read data4.txt, compute summary, write data5.txt

-- === Metatable (kept and hardened) ===
SummaryMetaTable = {
    __add = function(left, right)
      local newSummary = { super = 0, good = 0, middle = 0, low = 0 }
      for k, v in pairs(left) do
        newSummary[k] = (v or 0) + (right[k] or 0)
      end
      return newSummary
    end
  }
  
  -- === Helpers ===
  local function trim(s)
    return (s or ""):gsub("^%s+", ""):gsub("%s+$", "")
  end
  
  local function normalize_skill(s)
    s = trim(s):lower()
    if s == "super" or s == "good" or s == "middle" or s == "low" then
      return s
    end
    return "low"
  end
  
  -- === Find script directory (so paths are stable) ===
  local function script_dir()
    local src = debug.getinfo(1, "S").source
    if src:sub(1,1) == "@" then src = src:sub(2) end
    return src:match("^(.*[/\\])") or "./"
  end
  
  -- === Read input (with checks) ===
  -- adjust "../../" if your data4.txt sits elsewhere
  local infile = script_dir() .. "/data4.txt"
  print("Reading:", infile)
  
  local f, err = io.open(infile, "r")
  if not f then
    error("Cannot open input file '" .. infile .. "': " .. (err or "unknown error"))
  end
  
  local lines = {}
  for line in f:lines() do
    if trim(line) ~= "" then table.insert(lines, line) end
  end
  f:close()
  
  if #lines == 0 then error("Input file is empty.") end
  
  -- Skip header if present
  local first = lines[1]:lower()
  if first:find("name") and first:find("technical") then
    table.remove(lines, 1)
  end
  
  -- === Process rows ===
  local people = {}
  
  for _, line in ipairs(lines) do
    local name, tech, soft, bus, creative, academic =
      line:match("^%s*([^,]+)%s*,%s*([^,]+)%s*,%s*([^,]+)%s*,%s*([^,]+)%s*,%s*([^,]+)%s*,%s*([^,]+)%s*$")
  
    if not name then
      io.stderr:write("Skipping malformed line: " .. line .. "\n")
    else
      name     = trim(name)
      tech     = normalize_skill(tech)
      soft     = normalize_skill(soft)
      bus      = normalize_skill(bus)
      creative = normalize_skill(creative)
      academic = normalize_skill(academic)
  
      local summary = { super = 0, good = 0, middle = 0, low = 0 }
      setmetatable(summary, SummaryMetaTable)
  
      for _, skill in ipairs({ tech, soft, bus, creative, academic }) do
        summary[skill] = (summary[skill] or 0) + 1
      end
  
      local finalSummary
      if summary.super > 0 then
        finalSummary = "super"
      elseif summary.good >= 2 then
        finalSummary = "good"
      elseif summary.middle >= 3 then
        finalSummary = "middle"
      else
        finalSummary = "low"
      end
  
      table.insert(people, { name, tech, soft, bus, creative, academic, finalSummary })
    end
  end
  
  -- === Write output next to the script ===
  local outfile = script_dir() .. "data5.txt"
  local out, werr = io.open(outfile, "w")
  if not out then
    error("Cannot open output file '" .. outfile .. "': " .. (werr or "unknown error"))
  end
  
  out:write("Name,Technical Skills,Soft Skills,Business Skills,Creative Skills,Academic Skills,Summary\n")
  for _, entry in ipairs(people) do
    out:write(table.concat(entry, ",") .. "\n")
  end
  out:close()
  
  print("Wrote " .. tostring(#people) .. " row(s) to " .. outfile)
  
  
  
  