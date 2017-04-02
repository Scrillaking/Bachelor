package net.floodlightcontroller.mactracker;

import java.security.GeneralSecurityException;
import java.security.Key;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;


public class AES {

    public enum Mode {
        CBC, ECB, CFB, OFB, PCBC
    };

    public enum Padding {
        NoPadding, PKCS5Padding, PKCS7Padding, ISO10126d2Padding, X932Padding, ISO7816d4Padding, ZeroBytePadding
    }

    private static final String ALGORITHM = "AES";



    String decrypt(String valueToDec, Mode modeOption,
            Padding paddingOption,String SessionKey) throws GeneralSecurityException {



        byte[] decodeBase64 = java.util.Base64.getDecoder().decode(valueToDec.getBytes());
        byte[] keyValue = SessionKey.getBytes();
        Key key = new SecretKeySpec(keyValue, ALGORITHM); 
        Cipher c = Cipher.getInstance("AES/ECB/NoPadding"); 
        c.init(Cipher.DECRYPT_MODE, key); 
        byte[] encValue = c.doFinal(decodeBase64); 
        return new String(encValue).trim();

    }

}
