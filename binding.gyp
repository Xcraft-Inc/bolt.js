{
  "targets": [{
    "target_name": "bolt",
    "sources": ["build-go/bolt.cxx"],
    "libraries": ["../build-go/bolt.a"]
  }, {
    "target_name": "action_after_build",
    "type": "none",
    "dependencies": ["<(module_name)"],
    "copies": [{
      "files": ["<(PRODUCT_DIR)/<(module_name).node"],
      "destination": "<(module_path)"
    }]
  }]
}
