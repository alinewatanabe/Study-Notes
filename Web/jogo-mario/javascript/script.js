const cloud = document.querySelector('.cloud');
const cloud_2 = document.querySelector('.cloud_2');
const mario = document.querySelector('.mario');
const brick = document.querySelector('.brick');

const jump = () => {
    mario.classList.add('jump');
    setTimeout(() => {
        mario.classList.remove('jump');
    }, 850);
}

const loop = setInterval(() => {

    const brickPosition = brick.offsetLeft;
    const marioPosition = +window.getComputedStyle(mario).bottom.replace('px', '');
    const cloudPosition = cloud.offsetLeft;
    const cloud_2Position = cloud_2.offsetLeft;

    console.log(brickPosition);

    if(brickPosition < 110 && brickPosition > 0 && marioPosition < 55){ 
        brick.styles.animation = 'none';
        brick.styles.left = `${brickPosition}px`;

        mario.styles.animation = 'none';
        mario.styles.bottom = `${marioPosition}px`;

        cloud.styles.animation = 'none';
        cloud.styles.left = `${cloudPosition}px`;

        cloud_2.styles.animation = 'none';
        cloud_2.styles.left = `${cloud_2Position}px`;

        clearInterval(loop);
    }

}, 1);

document.addEventListener('keydown', jump);