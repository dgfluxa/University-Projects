package example.vego.com

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.view.View
import androidx.fragment.app.FragmentTransaction
import com.google.android.material.bottomnavigation.BottomNavigationView
import kotlinx.android.synthetic.main.fragment_scanner.*
import androidx.core.app.ComponentActivity
import androidx.core.app.ComponentActivity.ExtraData
import androidx.core.content.ContextCompat.getSystemService
import android.icu.lang.UCharacter.GraphemeClusterBreak.T
import android.widget.*


class VegoClassicMain : AppCompatActivity() {

    lateinit var homeFragment: HomeFragment
    lateinit var summaryFragment: SummaryFragment
    lateinit var scannerFragment: ScannerFragment
    lateinit var recommendationsFragment: RecommendationsFragment
    lateinit var profileFragment: ProfileFragment




    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_vego_classic_main)


        val bottomNavigation : BottomNavigationView = findViewById(R.id.btm_nav)

        homeFragment = HomeFragment()
        supportFragmentManager
            .beginTransaction()
            .replace(R.id.frame_layout, homeFragment)
            .setTransition(FragmentTransaction.TRANSIT_FRAGMENT_OPEN)
            .commit()

        bottomNavigation.setOnNavigationItemSelectedListener { item ->

            when (item.itemId) {

                R.id.home -> {

                    homeFragment = HomeFragment()
                    supportFragmentManager
                        .beginTransaction()
                        .replace(R.id.frame_layout, homeFragment)
                        .setTransition(FragmentTransaction.TRANSIT_FRAGMENT_OPEN)
                        .commit()
                }
                R.id.summary -> {

                    summaryFragment = SummaryFragment()
                    supportFragmentManager
                        .beginTransaction()
                        .replace(R.id.frame_layout, summaryFragment)
                        .setTransition(FragmentTransaction.TRANSIT_FRAGMENT_OPEN)
                        .commit()
                }
                R.id.scanner -> {

                    scannerFragment = ScannerFragment()
                    supportFragmentManager
                        .beginTransaction()
                        .replace(R.id.frame_layout, scannerFragment)
                        .setTransition(FragmentTransaction.TRANSIT_FRAGMENT_OPEN)
                        .commit()



                }
                R.id.recommendations -> {

                    recommendationsFragment = RecommendationsFragment()
                    supportFragmentManager
                        .beginTransaction()
                        .replace(R.id.frame_layout, recommendationsFragment)
                        .setTransition(FragmentTransaction.TRANSIT_FRAGMENT_OPEN)
                        .commit()
                    var recom_list = findViewById<ListView>(R.id.recom_list)
                }
                R.id.profile -> {

                    profileFragment = ProfileFragment()
                    supportFragmentManager
                        .beginTransaction()
                        .replace(R.id.frame_layout, profileFragment)
                        .setTransition(FragmentTransaction.TRANSIT_FRAGMENT_OPEN)
                        .commit()
                }

            }

            true


        }
    }

}
