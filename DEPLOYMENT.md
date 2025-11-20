# Deployment Guide - Sitcom Character Styles MCP Server

This guide covers deploying the sitcom-character-styles MCP server to FastMCP.cloud.

## Prerequisites

- GitHub account with repository access
- FastMCP.cloud account
- Python 3.10+ installed locally
- Git installed

## Local Testing

Before deployment, test the MCP server locally:

```bash
# Install dependencies
pip install -e .

# Run tests
pytest characters/

# Run MCP server locally
python -m sitcom_character_styles.mcp_server.server
```

The server should start on `http://localhost:5000/mcp`.

## Deployment Steps

### 1. Prepare Repository

```bash
# Clone or create repository
git clone https://github.com/dmarsters/sitcom-character-styles
cd sitcom-character-styles

# Ensure .gitignore is in place
cat .gitignore

# Check that pyproject.toml exists and is valid
cat pyproject.toml
```

### 2. Verify Package Structure

Required files for FastMCP deployment:

```
sitcom-character-styles/
├── pyproject.toml
├── README.md
├── .gitignore
├── sitcom_character_styles/
│   ├── __init__.py
│   ├── framework/
│   ├── characters/
│   └── mcp_server/
│       ├── __init__.py
│       └── server.py
└── characters/
    └── endora/
        ├── olog/
        ├── src/
        └── tests/
```

### 3. Update Version Numbers

If deploying a new version, update:
- `pyproject.toml`: `version = "X.Y.Z"`
- `sitcom_character_styles/__init__.py`: `__version__ = "X.Y.Z"`

### 4. Commit and Push to GitHub

```bash
# Stage all files
git add -A

# Commit with descriptive message
git commit -m "Add Phase 5: MCP Server with Endora operator"

# Push to main branch (or your working branch)
git push origin main
```

### 5. Deploy to FastMCP.cloud

**Option A: Using FastMCP Web Dashboard**

1. Go to https://fastmcp.cloud
2. Sign in to your account
3. Click "New Deployment" or "Add Server"
4. Select "GitHub" as source
5. Connect your GitHub account
6. Select repository: `dmarsters/sitcom-character-styles`
7. Configure deployment:
   - **Main entry point**: `sitcom_character_styles/mcp_server/server.py`
   - **Server class/function**: `server` (the FastMCP instance)
   - **Python version**: 3.10+
8. Click "Deploy"

**Option B: Using FastMCP CLI (if available)**

```bash
fastmcp deploy --repository dmarsters/sitcom-character-styles \
                --entry-point sitcom_character_styles/mcp_server/server.py \
                --server-object server
```

### 6. Verify Deployment

Once deployed, you should receive:
- Public MCP endpoint URL (e.g., `https://sitcom-character-styles.fastmcp.app/mcp`)
- Status confirmation

Test the endpoint:
```bash
curl https://sitcom-character-styles.fastmcp.app/mcp/health
```

### 7. Configure in Claude Desktop

Update your Claude Desktop MCP configuration:

**File location:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**Add to your config:**
```json
{
  "mcpServers": {
    "sitcom-character-styles": {
      "url": "https://sitcom-character-styles.fastmcp.app/mcp"
    }
  }
}
```

Restart Claude Desktop. The sitcom-character-styles tools should now be available.

### 8. Test in Claude

In Claude, ask:
```
"Enhance this prompt with Endora at intensity 7: 'a glass of wine on a windowsill'"
```

Claude will use the `enhance_prompt_with_endora_impl` tool from your deployed server.

## Monitoring and Updates

### Check Deployment Status

Visit the FastMCP dashboard to view:
- Deployment status
- Recent logs
- Usage statistics
- Error tracking

### Update the Server

To update the deployed server:

1. Make changes locally
2. Test thoroughly
3. Commit and push to GitHub
4. FastMCP will automatically redeploy (depending on configuration)

Or manually redeploy:
- In FastMCP dashboard, click "Redeploy" or "Rebuild"

### Troubleshooting

**Server won't start:**
- Check that `mcp_server/server.py` imports work locally
- Verify all dependencies are in `pyproject.toml`
- Check FastMCP logs for error messages

**Tools not available:**
- Ensure tool decorators use `@server.call_tool()`
- Check that tool functions have correct signatures
- Verify MCP endpoint is responding to list_tools request

**Transformation issues:**
- Test character operators locally first
- Check that prompts parse correctly
- Verify intensity values are 0-10

## Rollback

To rollback to previous version:

1. In FastMCP dashboard, find "Deployment History"
2. Select previous successful deployment
3. Click "Revert" or "Restore"

Or manually:
```bash
git checkout <previous-commit-hash>
git push origin main
# FastMCP will redeploy
```

## Next Steps

After successful deployment:

1. **Add Mork operator** (planned for Phase 5 continuation)
2. **Create character composition** (combining two characters' sensibilities)
3. **Implement natural transformations** (mathematically provable translations between character systems)
4. **Build academic publication** (formalizing the categorical approach)

## Support

For deployment issues:
- Check FastMCP.cloud documentation: https://fastmcp.app/docs
- Review MCP specification: https://modelcontextprotocol.io/
- GitHub issues: https://github.com/dmarsters/sitcom-character-styles/issues

## Success Criteria

Deployment is successful when:
- ✓ Server is running on FastMCP.cloud
- ✓ Public endpoint is accessible
- ✓ Tools are listed in MCP schema
- ✓ Claude can invoke tools
- ✓ Transformations produce correct output
- ✓ All intensity levels work (0-10)
- ✓ Transformation details are accurate when requested
