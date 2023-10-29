import { BsShareFill,BsFillTelephoneFill,BsFingerprint,BsFillQuestionDiamondFill } from 'react-icons/bs';
import { PiBankFill } from 'react-icons/pi';
import './css/Phone.css'
import './css/Login.css'
function Login() {
    return ( 
        <div className='app'>
            <div className="phone">
                <div className="phone__header">.</div>
                <div className="phone__main">
                    <div>
                        <div className='back'>X</div>
                        <div className='name'>
                            <PiBankFill/>
                            <span>AGRIBANK</span>
                        </div>
                        <div className='name__screen'>
                            Đăng nhập
                        </div>
                        <div>
                            <input className='input' placeholder="Số điện thoại                           0**********9"/>
                            <div className='vach'>.</div>
                            <input className='input' placeholder="Mật khẩu"/>
                            <div className='vach'>.</div>
                        </div>
                        <div className='xacthuc'>
                            <div className='button'>Đăng nhập</div>
                            <BsFingerprint className='vt'/>
                        </div>
                        <div className='qmk'>
                            Quên mật khẩu ?
                        </div>
                    </div>
                    <div className='bottom'>
                        <div>
                            <BsShareFill className='icon'/>
                            <span>Chia sẻ</span>
                        </div>
                        <div>
                            <BsFillQuestionDiamondFill className='icon'/>
                            <span>Hỏi đáp</span>
                        </div>
                        <div>
                            <BsFillTelephoneFill className='icon'/>
                            <span>Liên hệ</span>
                        </div>
                    </div>
                </div>
                <div className="phone__footer"></div>
            </div>
        </div>
     );
}

export default Login;