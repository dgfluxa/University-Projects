package example.vego.com

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AlertDialog


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val vego_classic_button = findViewById<Button>(R.id.VeGo_classic_button)
        val vego_health_button = findViewById<Button>(R.id.VeGo_health_button)

        vego_health_button.setOnClickListener {

            val builder = AlertDialog.Builder(this)

            builder.setTitle("Alert!")
            builder.setMessage("This feature is not ready yet")
            builder.setPositiveButton("Ok", null)

            val dialog : AlertDialog = builder.create()

            dialog.show()


        }

    }
    fun sendMessage(view: View) {
        val intent = Intent(this, VegoClassicMain::class.java)
        startActivity(intent)
    }
}
