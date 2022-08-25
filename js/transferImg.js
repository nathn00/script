const sharp = require("sharp");
const os = require("os");
const path = require("path");
const fs = require("fs");

const name = process.argv[2];
let startNumber = parseInt(process.argv[3]);
const homeDir = os.homedir();
const rawImgDir = path.join(
  homeDir,
  "Desktop/_Dev/labelme/examples",
  "raw_imgs"
);
const transferImgDir = path.join(
  homeDir,
  "Desktop/_Dev/labelme/examples",
  "custom"
);

fs.promises.readdir(rawImgDir).then(transferExt).then(resizer);

async function transferExt(files) {
  const maping = await files.map((file) => {
    const before = path.join(rawImgDir, file);
    const after = path.join(
      rawImgDir,
      `${name}_${startNumber.toString().padStart(2, "0")}.jpeg`
    );
    if (path.extname(file) === ".heic") {
      fs.rename(before, after, (err) => {
        if (err) throw err;
        console.log(`Transfer ${file} to JPEG.... SUCCESS!`);
      });
      startNumber += 1;
    }
    return after;
  });
  return maping;
}

function resizer(files) {}
